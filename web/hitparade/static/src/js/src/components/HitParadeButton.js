import React from 'react'; 
import PropTypes from 'prop-types';

const HitParadeButton = props => {
  return (
            <button className={props.className} onClick={() => props.clickMethod()}>
            		{props.buttonText}
            </button>
        );
}
HitParadeButton.propTypes = {
	className: PropTypes.string.isRequired,
	buttonText: PropTypes.string.isRequired,
	clickMethod: PropTypes.func.isRequired,
};

export default HitParadeButton;