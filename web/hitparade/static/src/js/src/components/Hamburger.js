import React, { PropTypes } from 'react';

const MobileDrawer = props => {
  return (
            <div 
				className={`hamburger ${props.isOpen ? 'open' : ''} ${props.className || ''} `}
				onClick={(e) => {
					if (props.onClick) {
						props.onClick(e);
					}
				}}
			>
            		<div className="line line-1"></div>
            		<div className="line line-2"></div>
            		<div className="line line-3"></div>
            		<div className="line line-4"></div>
            </div>
        );
}
MobileDrawer.propTypes = {
	className: PropTypes.string,
	isOpen: PropTypes.bool,
};

export default MobileDrawer;