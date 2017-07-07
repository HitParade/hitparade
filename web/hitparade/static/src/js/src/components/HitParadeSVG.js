import React from 'react'; 
import PropTypes from 'prop-types';

const HitParadeSVG = props => {
  return (
            <div className={props.className} onClick={() => props.clickMethod()}>
            		<img src={props.svg} style={{height: props.height, width: props.width}} />
            </div>
        );
};
HitParadeSVG.propTypes = {
	className: PropTypes.string.isRequired,
	svg: PropTypes.string.isRequired,
	width: PropTypes.string.isRequired,
	height: PropTypes.string.isRequired,
	clickMethod: PropTypes.func,
};

export default HitParadeSVG;