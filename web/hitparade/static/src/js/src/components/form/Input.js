import React, { Component, PropTypes } from 'react';


class TextInput extends Component {
  static propTypes = {
    label: PropTypes.string,
    note: PropTypes.string,
    idName: PropTypes.string,
    type: PropTypes.string,
    inputClass: PropTypes.string,
    value: PropTypes.string,
    placeholder: PropTypes.string,
    name: PropTypes.string,
    parentClass: PropTypes.string,
    onChange: PropTypes.func,
    onFocus: PropTypes.func,
    onBlur: PropTypes.func,
    onKeyUp: PropTypes.func,
    error: PropTypes.bool,
    errorMessage: PropTypes.string,
    valid: PropTypes.bool,
  };

  render() {
    const {
        label,
        idName,
        type,
        value,
        placeholder,
        onChange,
        onFocus,
        onBlur,
        onKeyUp,
        parentClass,
        name,
        error,
        errorMessage,
        valid,
      } = this.props;

    let {
      inputClass,
      } = this.props;

    if (error) {
      inputClass += ' has-error';
    }

    if (valid) {
      inputClass += ' is-valid';
    }

    return (
      <div className={`component text-input ${parentClass || ''}`}>
        <label htmlFor={idName}>{label}</label>
        <input
          id={idName}
          className={inputClass}
          name={name}
          type={type}
          value={value}
          placeholder={placeholder}
          onChange={(e) => onChange(e.target.value)}
          onFocus={onFocus}
          onBlur={onBlur}
          onKeyUp={onKeyUp}
          ref={`input_${name}`}
        />
        <div className="error-message">{errorMessage}</div>
      </div>
    );
  }
}


export default TextInput;
