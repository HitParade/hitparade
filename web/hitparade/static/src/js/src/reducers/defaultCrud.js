import _ from 'lodash';
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
        if (_.isArray(action.data)) {
          state = state.mergeDeep(_.keyBy(action.data, 'id'));
        } else if (_.isObject(action.data)) {

          let val = {};
          val[action.data.id] = action.data;
          state = state.mergeDeep(val);
        }

        return state;
      },

      [DELETE]: (state, action) => {

        // will merge an array of items or an individual object
        if (_.isArray(action.data)) {
          action.data.forEach((key) => {
            state = state.delete(key);
          });
        } else {
          state = state.delete(actoin.data);
        }

        return state;
      }
    }
  }
};


export default defaultCrud;
