import _ from 'lodash';
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

const actionTypsActionCreators = _.fromPairs(
    _.map(ActionTypes, (type) =>  [_.camelCase(type), createAction(type)])
);

const actionPartialsActionCreators = _.fromPairs(
    _.reduce(Reducers, (arr, type) =>  {
        let upperCaseType = type.toUpperCase()
        let updateAction = `${upperCaseType}${ActionPartials._CREATE_OR_UPDATE}`;
        let deleteAction = `${upperCaseType}${ActionPartials._DELETE}`;
       arr.push([_.camelCase(updateAction), createAction(updateAction)]);
       arr.push([_.camelCase(deleteAction), createAction(deleteAction)]);

       return arr;
    },[])
);

const actionCreators = _.merge(actionTypsActionCreators, actionPartialsActionCreators);

export default actionCreators;