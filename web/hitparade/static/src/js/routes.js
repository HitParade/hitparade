import React from 'react';
import { Route } from 'react-router';
import App from './src/containers/App';
import HitParade from './src/containers/HitParade';
import Test from './src/containers/Test';

function loadRoute(cb) {
  return module => cb(null, module.default);
}

function errorLoading(error) {
  throw new Error(`Dynamic page loading failed: ${error}`);
}

export const routePaths = {
  base: '/',
  test: '/app/test'
}

export const routes = (
  <Route component={App}>
    <Route path={routePaths.base} getComponent={(location, cb) => {
        import(/* webpackMode: "lazy" */'./src/containers/HitParade')
          .then(loadRoute(cb, false))
          .catch(errorLoading);
      }}/>
    <Route path={routePaths.test} getComponent={(location, cb) => {
        import(/* webpackMode: "lazy" */'./src/containers/Test')
          .then(loadRoute(cb, false))
          .catch(errorLoading);
      }}/>
  </Route>
);
