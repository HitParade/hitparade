import isArray from 'lodash/isArray';
import keyBy from 'lodash/keyBy';
import isObject from 'lodash/isObject';
import Immute from 'object-path-immutable';
import {
  _DELETE,
  _CREATE_OR_UPDATE
} from '../constants/ActionPartials';

/**
 * For Immutable.orderedMap();
 * @param reducerName
 * @returns {{}}
 */
const defaultCrud = function (reducerName) {
const CREATE_OR_UPDATE = `${reducerName.toUpperCase()}${_CREATE_OR_UPDATE}`;
const DELETE = `${reducerName.toUpperCase()}${_DELETE}`;

  return {
    actions: {
      [`${reducerName.toUpperCase()}${_CREATE_OR_UPDATE}`]: (state, action) => {
        // will merge an array of items or an individual object
        if ( isArray(action.data)) {
          state = Immute.set(state,  keyBy(action.data, 'id'))
        } else if ( isObject(action.data)) {

          let val = {};
          val[action.data.id] = action.data;
          state = Immute.set(state, val);
        }

        return state;
      },

      [DELETE]: (state, action) => {
        state = Immute.set(state);
        // will merge an array of items or an individual object
        if ( isArray(action.data)) {
          action.data.forEach((key) => {
            delete state[key] ;
          });
        } else {
          delete state[actoin.data];
        }

        return state;
      }
    }
  }
};


export default defaultCrud;
