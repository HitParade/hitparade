import fromPairs from 'lodash/fromPairs';
import map from 'lodash/map';
import camelCase from 'lodash/camelCase';
import merge from 'lodash/merge';
import reduce from 'lodash/reduce';
import * as ActionTypes from '../constants/ActionTypes';
import * as ActionPartials from '../constants/ActionPartials';
import * as Reducers from '../constants/Reducers';


/**
 * creates equivilant function as:
 * 
 * function functionName(data) {
 *  return {
 *    type: types.ACTION_TO_PERFORM,
 *    data,
 *  };
 * }
 */
const createAction = (type) => {
    return (data) => {
       return {type, data};
    }
}

const actionTypsActionCreators =  fromPairs(
     map(ActionTypes, (type) =>  [ camelCase(type), createAction(type)])
);

const actionPartialsActionCreators =  fromPairs(
     reduce(Reducers, (arr, type) =>  {
        let upperCaseType = type.toUpperCase()
        let updateAction = `${upperCaseType}${ActionPartials._CREATE_OR_UPDATE}`;
        let deleteAction = `${upperCaseType}${ActionPartials._DELETE}`;
       arr.push([ camelCase(updateAction), createAction(updateAction)]);
       arr.push([ camelCase(deleteAction), createAction(deleteAction)]);

       return arr;
    },[])
);

const actionCreators =  merge(actionTypsActionCreators, actionPartialsActionCreators);

export default actionCreators;