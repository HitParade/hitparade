import thunk from 'redux-thunk';
import { 
  syncHistoryWithStore, 
  routerMiddleware 
} from 'react-router-redux';

import { 
  browserHistory 
} from 'react-router';

import { 
  createStore, 
  combineReducers,
  applyMiddleware,
  compose
} from 'redux';

import rootReducer from '../reducers';
import DevTools from '../containers/DevTools';

const router = routerMiddleware(browserHistory);

const configureStore = (preloadedState) =>
    createStore(
        rootReducer,
        compose(
        applyMiddleware(thunk, router),
            DevTools.instrument(),
        )
    );


export default configureStore;