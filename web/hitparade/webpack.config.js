var path = require('path');
var fs = require('fs');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');
var BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

var sourcePath = path.join(__dirname, './static/src');

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
    new webpack.DefinePlugin({
      __DEV__: false,
      'process.env': {
        NODE_ENV: JSON.stringify('development')
      }
    }),
    new webpack.optimize.CommonsChunkPlugin({
      // name: 'vendor',
      // filename: 'js/vendor.js',
      // minChunks(module) {
      //   const context = module.context;
      //   return context && context.indexOf('node_modules') >= 0;
      // },
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
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        screw_ie8: true,
        warnings: false
      }
    }),
    /* run on dev build only */
    new BundleAnalyzerPlugin({
            analyzerMode: 'static'
    }),
    new ExtractTextPlugin('css/site.css')
  ],

};
