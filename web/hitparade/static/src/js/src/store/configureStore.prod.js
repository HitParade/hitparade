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
} from 'redux';

import rootReducer from '../reducers';

const router = routerMiddleware(browserHistory);

const configureStore = (preloadedState) =>
    createStore(
        rootReducer,
        applyMiddleware(thunk, router)
    );


export default configureStore;