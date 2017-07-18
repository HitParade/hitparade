import React from 'react';
import { render } from 'react-dom';
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';
import configureStore from './src/store/configureStore';
import { 
  syncHistoryWithStore, 
} from 'react-router-redux';

import { 
  Router,
  browserHistory 
} from 'react-router';

import { routes } from './routes';
import '../scss/site.scss';

const store = configureStore();

const history = syncHistoryWithStore(browserHistory, store);

const showDevToolsWindow = true;
if (process.env.TIER === 'dev' && showDevToolsWindow) {
  const createDevToolsWindow = require('./utils/createDevToolsWindow').default;
  createDevToolsWindow(store);
}

render(
    <Provider store={store}>
        <Router history={history} routes={routes}/>
    </Provider>,
  document.getElementById('root')
);