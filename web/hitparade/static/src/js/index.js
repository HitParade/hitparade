import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { Router } from 'react-router';

import { browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';

import { createStore, combineReducers } from 'redux';
import { routes } from './routes';
// import HitParadeReducer from './src/reducers/hitparade';
// import HitParade from './src/containers/HitParade';
import rootReducer from './reducers';
import '../scss/site.scss';

const store = createStore(
  rootReducer,
  // HitParadeReducer,
  window.devToolsExtension && window.devToolsExtension()
);

const history = syncHistoryWithStore(browserHistory, store);

render(
    <Provider store={store}>
        {/*<HitParade />*/}
        <Route history={history} routes={routes}/>
    </Provider>,
  document.getElementById('root')
);