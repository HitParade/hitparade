import React, { PropTypes } from 'react';

const HitParadeLeftMenuItem = props => {
  const svg_value = props.svg?<img src={props.imgRoot +props.svg.img} style={{width: props.svg.width ,height: props.svg.height, maxHeight: props.svg.maxHeight}} />:undefined;
  const menuItemText = props.menuItemText;
  const classNames = props.classNames?props.classNames:"hp-header-item proxima-nova-regular";
  let onClickMethod = props.clickMethod;
  return (
            <div className={classNames} onClick={() => onClickMethod()}>
              <div className="hp-header-item-text">{menuItemText}</div>
             {svg_value}
            </div>
        );
}
HitParadeLeftMenuItem.propTypes = {
	svg: PropTypes.object,
	menuItemText: PropTypes.string.isRequired,
    clickMethod: PropTypes.func.isRequired,
    classNames: PropTypes.string,
};

export default HitParadeLeftMenuItem;