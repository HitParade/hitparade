import actions from './ActionCreators';
import _ from 'lodash';
/**
 * Form validation
 */
const validationFuncs = {
  email: (value) => /^([a-z0-9+_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,24})$/.test(value),
  passLength: (value) => /^[a-zA-Z0-9+_-]{6,18}$/.test(value),
  required: (value) => !!value,
}

const validationErrorMessages = {
  email: 'Must be a valid email.',
  passLength: 'Password must be at least 6 characters.',
  required: 'Field is required.',
}

let errorMessages = {};

/**
 * Runs the valiation functions from validationFuncs on the
 * input values and adds error messages if errors.
 *
 * @param fieldName
 * @param fieldValue
 * @param validationArr
 * @returns {boolean}
 */
function validate(fieldName, fieldValue, validationArr) {
  let isValid = true;
  let validationMessage;

  validationArr.forEach((validationKey) => {
    // TODO if wrong validation key throw error
    if (!validationFuncs[validationKey](fieldValue)) {
      isValid = false;
      validationMessage = validationErrorMessages[validationKey];
      if (errorMessages[fieldName]) {
        errorMessages[fieldName].push(validationMessage);
      } else {
        errorMessages[fieldName] = [validationMessage];
      }
    }
  });

  return isValid;
}

/**
 * Iterates the inputs recursively if container component
 * @param formInputs
 * @param callBack
 */
function iterateInputFields(formInputs, callBack) {
  formInputs.forEach((field) => {
    if (field.formInputs) {
      iterateInputFields(field.formInputs, callBack);
    }
    else if (field.validate) {
      callBack(field.name, field.validate);
    }
  });
}

/**
 * Validates the inputs that have the validate key.
 *
 * @param formName
 * @param formInputs
 * @returns {Function}
 */
export function validateInputs(formName, formInputs) {
  return (dispatch, getState) => {
    errorMessages = {};
    const forms = getState().forms;
    const form = forms[formName];
    let isAllValid = true;
    let message;
    let isValid;

    iterateInputFields(formInputs, (name, validationArr) => {
      if (!validationArr.length) {
        return;
      }

      message = '';
      isValid = validate(name, _.get(form, name, 'default'), validationArr);
      if (!isValid) {
        isAllValid = false;
        message = errorMessages[name] || '';
      }

      dispatch(actions.updateField({
        formName: `error${formName}`,
        name,
        value: message && message.join(' '),
      }));
    });

    return isAllValid;
  };
}


export function getFormContent(formName) {
  return (dispatch, getState) => {
    const forms = getState().forms;
    return forms[formName];
  };
}
