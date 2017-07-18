/* eslint-disable no-unused-vars */
import createReducer from '../../utils/createReducer';
import Immute from 'object-path-immutable';

import {
  UPDATE_FIELD,
  CLEAR_FORM,
} from '../constants/ActionTypes';


const forms = {
  state: {}, 
  actions: {
    [UPDATE_FIELD]: (state, action) => {
      const { formName, name, value } = action.data;
      const newState = Immute.set(state, `${formName}.${name}`, value)
      return newState;
    },

    [CLEAR_FORM]: (state, action) => {
      const formName = action.data;
      const newState = { ...state }
      newState[formName] = {}
      newState[`error${formName}`] = {};
      return newState;
    },
  }
};


export default forms;
