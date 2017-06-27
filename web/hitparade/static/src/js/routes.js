import React from 'react';
import { Route } from 'react-router';
import App from './src/containers/App';
import HitParade from './src/containers/HitParade';

export const routePaths = {
  base: '/'
}

export const routes = (
  <Route component={App}>
    <Route path={routePaths.base} component={HitParade}/>
    <Route path={'app/test'} component={(<div>hello</div>)}/>
  </Route>
);
