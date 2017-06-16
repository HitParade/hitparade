var path = require('path');
var fs = require('fs');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');

module.exports = {
  devtool: 'source-map',
  entry: './static/src/js/index.js',
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loaders: ['babel-loader'],
        exclude: /node_modules/,
      }, 
      {
        test: /\.json$/,
        loader: 'json-loader'
      },
      {
        test: /\.js$/,
        loaders: ['babel'],
        exclude: /node_modules/,
      },
      {
        test: /\.scss?$/,
        /**
         * css-loader integrates cssnano.
         * The ExtractTextPlugin extracts the css file
         */
        loader: ExtractTextPlugin.extract('style-loader', 'css-loader!postcss-loader!sass-loader'),
      },
    ],
    noParse: /node_modules\/json-schema\/lib\/validate\.js/
  },
  // static/dist/js/site.
  output: {
    path: path.join(__dirname, 'static/dist'),
    filename: 'js/site.js',
    publicPath: '../static/dist/'
  },
  resolve: {
    modules: [path.resolve(__dirname, 'app'), 'node_modules'],
    root: path.resolve('./static/src'),
    extensions: ['', '.js', '.jsx'],
    packageMains: ['webpack', 'browser', 'web', 'browserify', ['jam', 'main'], 'main']
  },
  externals: [
  ],
  plugins: [
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.DefinePlugin({
      __DEV__: false,
      'process.env': {
        NODE_ENV: JSON.stringify('production')
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        screw_ie8: true,
        warnings: false
      }
    }),
    // new webpack.LoaderOptionsPlugin({ options: { postcss: [ autoprefixer ] } }),
    new ExtractTextPlugin('css/site.css')
  ],

};
