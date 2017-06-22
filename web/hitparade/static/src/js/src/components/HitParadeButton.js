import React, { PropTypes } from 'react';

const HitParadeButton = props => {
  return (
            <button className={props.className} onClick={() => props.onClick()}>
            		{props.buttonText}
            </button>
        );
}
HitParadeButton.propTypes = {
	className: PropTypes.string.isRequired,
	buttonText: PropTypes.string.isRequired,
	onClick: PropTypes.func.isRequired,
};

export default HitParadeButton;