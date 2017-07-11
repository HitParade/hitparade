import React from 'react'; 
import PropTypes from 'prop-types';

const SubmitButton = props => {
  const { onClick, isLoading, text, className } = props;
    return (
      <button
        className={`component submit-button ${className} ${isLoading ? 'loading' : ''}`}
        onClick={e => onClick(e)}
      >
        {isLoading && <figure className="loadera">Loading...</figure> }
        {!isLoading && text}
      </button>
    )
}

SubmitButton.propTypes = {
    isLoading: PropTypes.bool,
    onClick: PropTypes.func,
    text: PropTypes.string,
    children: PropTypes.any,
    className: PropTypes.string,
};

export default SubmitButton;