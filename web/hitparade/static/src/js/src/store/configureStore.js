if (process.env.NODE_ENV === 'prod' || process.env.NODE_ENV === 'test') {
  module.exports = require('./configureStore.prod');
} else {
  module.exports = require('./configureStore.dev');
}