import React from 'react';
import { render } from 'react-dom';
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';
import { 
  syncHistoryWithStore, 
  routerMiddleware 
} from 'react-router-redux';

import { 
  Router,
  browserHistory 
} from 'react-router';

import { 
  createStore, 
  combineReducers,
  applyMiddleware 
} from 'redux';

import { routes } from './routes';
import rootReducer from './src/reducers';
import '../scss/site.scss';

const router = routerMiddleware(browserHistory);

const store = createStore(
  rootReducer,
  applyMiddleware(thunk, router),
  // window.devToolsExtension && window.devToolsExtension()
);

const history = syncHistoryWithStore(browserHistory, store);

render(
    <Provider store={store}>
        <Router history={history} routes={routes}/>
    </Provider>,
  document.getElementById('root')
);