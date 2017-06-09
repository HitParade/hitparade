import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, combineReducers } from 'redux';
import HitParadeReducer from './src/reducers/hitparade';
import HitParade from './src/containers/HitParade';
import '../scss/site.scss';

const store = createStore(
  HitParadeReducer,
  window.devToolsExtension && window.devToolsExtension()
);
render(
    <Provider store={store}>
        <HitParade />
    </Provider>,
  document.getElementById('root')
);