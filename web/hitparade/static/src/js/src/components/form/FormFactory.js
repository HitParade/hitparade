import React, { Component, PropTypes } from 'react';
import _ from 'lodash';
import Input from './Input';
import SubmitButton from './SubmitButton';
import Link from './Link';
// import Information from 'components/form/Information';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
// import FormFactory from 'components/form/FormFactory';
import * as FormActions from '../../actions/forms';
import Actions from '../../actions/ActionCreators';


/**
 * ** IMPORTANT** when importing use the container component:
 * import FormFactory from 'containers/FormFactoryContainer';
 *
 *
 * Form Factory:
 * Pass an array of input configs to quickly spin
 * up a form.
 *
 * basic usage as react element
 * <FormFactory
 *  formName={formName}
 *  className="simplifeye-form-elements"
 *  formInputs={formInputs}
 *  submit={submit}
 * />
 *
 * formName: is a the unique name of the form.
 * className: optional.
 * formInputs: the configuration of form elements. more below.
 * submit: the submit function that runs on click of the submit button.
 *
 * If there is a need for custom form elements pass in an object
 * in the key alternateInputs with keys ass the form types and
 * values as the element constructors.
 *
 * formName:
 * This is a required prop because it creates a unique key in state.forms.
 * The values for the form inputs are stored under this key and populate
 * the form inputs values.
 *
 * Errors are captured in the same way under state.forms.errorsYourFormName.
 * See reducer/forms.js and actions/forms.js
 *
 * Form Inputs:
 * Generally all values in the form config objects will be passed as
 * props to the form elements. so if you need an onClick or some unique value,
 * add it to the form config object.
 *
 * example form input configs:
 *
 * let formInputs = [
 *  {
 *    type: 'email',
 *    label: 'Username',
 *    name: 'username',
 *    placeholder: 'Username'
 *  },
 *  {
 *    type: 'password',
 *    label: 'Password',
 *    name: 'password',
 *    information: 'some info' // this can be passed to get an info icon and
 * bubble placeholder: 'Password'
 *  }
 * ];
 *
 * The name field can be a space separated list of values.
 * This will nest the name and input value one level for
 * each value added to the list.
 *
 * This allows nesting multiple input fields under one key
 * example:
 *
 * let formInputs = [
 *  {
 *    type: 'email',
 *    label: 'Username',
 *    name: 'userInfo.username',
 *    placeholder: 'Username'
 *  },
 *  {
 *    type: 'password',
 *    label: 'Password',
 *    name: 'userInfo.password',
 *    placeholder: 'Password'
 *  }
 * ];
 *
 * output after user has entered information:
 *
 * {
 *    userInfo: {
 *                username: 'mr_poopy_pants'
 *                password: 'not your biz'
 *               }
 * }
 *
 * There are other types that can be passed as objects in the form config.
 *  other types:
 *      container     - contains several inputs to create columns with, for
 * example a two-column class button        - creates a button link          -
 * creates a link element submitButton  - this button will be passed the submit
 * function
 *
 *
 * Adding a submit button.
 * the submit function should not be passe to the submit button
 * {
 *  type: 'submitButton'
 *  text: 'submit'
 * }
 *
 * Container example:
 * }
 *  type: 'container',
 *  className: 'two-column',
 *  formInputs: [
 *    {
 *      type: 'email',
 *      label: 'Username',
 *      name: 'username.first', // can do deep nesting
 *      placeholder: 'Username',
 *    },
 *    {
 *      type: 'email',
 *      label: 'Username',
 *      name: 'username',
 *      placeholder: 'Username',
 *    },
 *    {
 *      type: 'button',
 *      text: 'Sign In',
 *      className: 'sf-button',
 *    },
 *  ],
 * },
 *
 * For other important pieces to FormFactory:
 * See actions/forms
 * See reducres/forms
 *
 */

class FormFactory extends Component {
  static propTypes = {
    formInputs: PropTypes.array.isRequired,
    formName: PropTypes.string.isRequired,
    submit: PropTypes.func.isRequired,
    submitButtonText: PropTypes.string,
    className: PropTypes.string,
    updateField: PropTypes.func,
    validateInputs: PropTypes.func,
    getFormContent: PropTypes.func,
    isLoading: PropTypes.bool,
    children: PropTypes.any,
    formsState: PropTypes.object,

    // Object of alternate input constructors.
    alternateInputs: PropTypes.object,
  };

  componentWillMount() {
    const { formInputs } = this.props;
    this.setInitialValues(formInputs);
  }

  setInitialValues(formInputs) {
    return formInputs.forEach((item, i) => {
      if (item.type === 'container') {
        return this.setInitialValues(item.formInputs);
      }

      if (item.name) {
        this.childOnChange(item.name, item.value || '');
      }
    });
  }

  getInputs() {
    return {
      textInput: Input,
      button: SubmitButton,
      submitButton: SubmitButton,
      link: Link,
    //   information: Information,
    };
  }

  /**
   * Gets the input constructor.
   *
   * @param type
   * @returns {*}
     */
  getInput(type) {
    let inputType = type;
    const inputs = this.getInputs();
    const alternateInputs = this.props.alternateInputs;

    // text email and password share the same type of input
    const textInputReg = /text|email|password/g;
    if (textInputReg.test(inputType)) {
      inputType = 'textInput';
    }

    // choose from custom inputs or generic inputs
    return alternateInputs && alternateInputs[inputType] || inputs[inputType];
  }

  /**
   * Run on click of submit button.
   * @param e
   */
  submit(e) {
    e.preventDefault();
    const { submit, validateInputs, formName, formInputs, getFormContent } = this.props;
    const isValid = validateInputs(formName, formInputs);
    const formContent = getFormContent(formName);

    if (isValid) {
      submit(formContent);
    }
  }

  createElement(el, props, children) {
    return React.createElement(el, props, children);
  }

  /**
   * On change function to be passed to form inputs
   * @param name
   * @param value
   */
  childOnChange(name, value) {
    const { updateField, formName } = this.props;
    updateField({ formName, name, value });
  }

  /**
   * Adds a container if you want multiple columns.
   * the input className can be:
   *    two-column
   *    three-column
   *    four-column
   *
   * @param item
   * @returns {XML}
     */
  renderContainer(item, i) {
    const inputs = this.renderFormInputs(item.formInputs);

    return (
      <div
        key={item.className + i}
        className={`ff-container ${item.className}`}
      >
        {inputs}
      </div>
    );
  }

  /**
   * Renders inputs from config
   * @returns {*}
   */
  renderFormInputs(formInputs) {
    const { formsState, formName } = this.props;

    let values;
    let errors;
    let el;

    if (formsState) {
      values = formsState[formName];
      errors = formsState[`error${formName}`];
    }
    let inputEl;
    let props;

    // create elements of form inputs
    return formInputs.map((item, i) => {
      if (item.type === 'container') {
        return this.renderContainer(item, i);
      }

      inputEl = this.getInput(item.type);
      if (inputEl) {
        // these props will get passed to all form elements
        props = {
          ...item,
          error: errors && !!_.get(errors, item.name),
          errorMessage: errors && _.get(errors, item.name),
          value: values && _.get(values, item.name) || item.value || '',
          key: i,
          onChange: (value) => this.childOnChange(item.name, value),
        }

        if (item.type === 'submitButton') {
          props.onClick = this.submit.bind(this);
        }

        el = this.createElement(inputEl, props);

        if (item.information) {
          el = this.createElement(Information, { key: item.name, text: item.information }, el);
        }

        return el;
      }

      return null;
    });
  }

  render() {
    const { formInputs, className } = this.props;
    return (
      <div className={`component-form-factory ${className}`}>
        {this.renderFormInputs(formInputs)}
      </div>
    );
  }
}


const mapStateToProps = (state) => {
  return {
    formsState: state.forms,
  };
}

const mapDispatchToProps = (dispatch) => {
  const actions = {
    updateField: Actions.updateField,
    validateInputs: FormActions.validateInputs,
    getFormContent: FormActions.getFormContent,
  };

  return bindActionCreators(actions, dispatch);
};

export default connect(mapStateToProps, mapDispatchToProps)(FormFactory);
