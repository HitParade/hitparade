import React, { PropTypes } from 'react';

const MobileDrawer = props => {
  return (
            <div className={`mobile-drawer ${props.isOpen ? 'open' : ''}`}>
            		{props.children}
            </div>
        );
}
MobileDrawer.propTypes = {
	className: PropTypes.string,
	isOpen: PropTypes.bool,
};

export default MobileDrawer;