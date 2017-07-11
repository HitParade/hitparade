import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import FormFactory from '../components/form/FormFactory';
import { TEST_FORM } from '../constants/Forms';


const getInputs = [
      {
        type: 'container',
        className: 'three-column',
        formInputs: [
          {
            type: 'text',
            label: 'First Name',
            name: 'first_name', // can do deep nesting
            placeholder: 'First Name',
            validate: ['required'],
          },
          {
            type: 'text',
            label: 'Last Name',
            name: 'last_name',
            placeholder: 'Last name',
            validate: ['required'],
          },
          {
            type: 'email',
            label: 'Email',
            name: 'username',
            placeholder: 'Email',
            validate: ['required', 'email'],
          },
        ],
      },
      {
        type: 'container',
        className: 'three-column',
        formInputs: [
          {
            type: 'dropDownOther',
            name: 'role',
            placeholder: 'Select a role',
            showOther: true,
            validate: ['required'],
            list: [
              'Doctor',
              'Assistant',
              'Hygenist',
            ],
          },
          {
            type: 'dropDownOther',
            name: 'watch_user',
            placeholder: 'Is a watch user?',
            validate: ['required'],
            list: [
              'Yes',
              'No',
            ],
          },
          {
            type: 'submitButton',
            text: 'Add user',
            className: 'sf-button',
          },
        ],
      },
    ];
class Test extends Component {
  render() {
    return (
      <div>
         <FormFactory
            formName={TEST_FORM}
            formInputs={getInputs}
            submit={() => { console.log('submitted')}}
        />
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {};
}

function mapDispatchToProps(dispatch) {
  return {} //bindActionCreators(session, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Test);
