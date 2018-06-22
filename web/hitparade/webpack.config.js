require('dotenv').config({ path: '../.env', silent: true });

var path = require('path');
var fs = require('fs');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');
var BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

var sourcePath = path.join(__dirname, './static/src');
var files = fs.readdirSync(__dirname);



let plugins = [];

if (process.env.TIER === 'dev') {
  plugins = [
    /* run on dev build only */
    new BundleAnalyzerPlugin({
        analyzerMode: 'static',
        reportFilename: 'webpack_bundle_analyser_report.html',
    }),
  ]
} else {
  plugins = [
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        screw_ie8: true,
        warnings: false
      }
    }),
  ]
}


var tier = process.env.TIER;
module.exports = {
  devtool: 'source-map',
  entry: './static/src/js/index.js',
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: [
          'babel-loader',
        ],
      }, 
      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader!postcss-loader!sass-loader',
        }),
      }
    ],
    noParse: /node_modules\/json-schema\/lib\/validate\.js/
  },
  output: {
    path: path.join(__dirname, 'static/dist'),
    filename: 'js/site.js',
    publicPath: '../static/dist/'
  },
  resolve: {
    modules: [path.resolve(__dirname, 'app'), 'node_modules'],
    extensions: ['.js', '.jsx'],
  },
  externals: [
  ],
  plugins: [
    ...plugins,
    new webpack.DefinePlugin({
      __DEV__: false,
      'process.env': {
        TIER: JSON.stringify(tier),
      }
    }),
    new webpack.optimize.CommonsChunkPlugin({
       name: 'vendor',
        minChunks: Infinity,
        filename: 'js/[name].js',
    }),
    new webpack.LoaderOptionsPlugin({
      options: {
        postcss: [
          autoprefixer({
            browsers: [
              'last 3 version',
              'ie >= 10',
            ],
          }),
        ],
        context: sourcePath,
      },
    }),
    new ExtractTextPlugin('css/site.css')
  ],

};
