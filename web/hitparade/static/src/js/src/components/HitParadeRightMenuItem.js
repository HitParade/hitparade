import React from 'react'; 
import PropTypes from 'prop-types';

const HitParadeRightMenuItem = props => {
  const svg_value = props.svg?<img src={props.imgRoot + props.svg.img} style={{width: props.svg.width ,height: props.svg.height, maxHeight: props.svg.maxHeight}} />:undefined;
  const menuItemText = props.menuItemText;
  return (
            <div className="hp-right-header-item proxima-nova-regular">
             <div className="hp-header-item-text">{menuItemText}</div>
             {svg_value}
            </div>
        );
}
HitParadeRightMenuItem.propTypes = {
	svg: PropTypes.object,
	menuItemText: PropTypes.string.isRequired,
};

export default HitParadeRightMenuItem;