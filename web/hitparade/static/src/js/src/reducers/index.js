import { combineReducers } from 'redux';
import { routerReducer as routing } from 'react-router-redux';
import map from 'lodash/map';
import fromPairs from 'lodash/fromPairs';
import merge from 'lodash/merge';
import * as reducerConst from '../constants/Reducers';
import createReducer from '../../utils/createReducer';
import defaultCrud from './defaultCrud';
import hitParade from './hitParade';
import forms from './forms';


const combineReducerConfigs = {
    hitParade,
    forms
}

// create default actions for reducer constatns
const reducerDefaultCRUD =  fromPairs(
     map(reducerConst , reducer =>  [reducer, defaultCrud(reducer)])
);

// merge all reducer configs
const reducersReadyToBeCreated =  merge(reducerDefaultCRUD, combineReducerConfigs)

// create reducers
const createdReducers =  fromPairs(
   map(reducersReadyToBeCreated, (reducerConfig, reducerName) => {
    return [reducerName, createReducer(reducerConfig.state || {}, reducerConfig.actions)]
  })
);

const rootReducer = combineReducers({
    ...createdReducers, 
    routing
});


export default rootReducer;
