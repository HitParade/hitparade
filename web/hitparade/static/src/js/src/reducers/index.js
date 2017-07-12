import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import _ from 'lodash';
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
const reducerDefaultCRUD = _.fromPairs(
    _.map(reducerConst , reducer =>  [reducer, defaultCrud(reducer)])
);

// merge all reducer configs
const reducersReadyToBeCreated = _.merge(reducerDefaultCRUD, combineReducerConfigs)

// create reducers
const createdReducers = _.fromPairs(
  _.map(reducersReadyToBeCreated, (reducerConfig, reducerName) => {
    return [reducerName, createReducer(reducerConfig.state || {}, reducerConfig.actions)]
  })
);

const rootReducer = combineReducers({
    ...createdReducers, 
    routerReducer
});


export default rootReducer;
