import React, { PropTypes } from 'react';
import SocialMediaShare from './SocialMediaShare';

const MobileDrawerContent = props => {
  return (
            <div 
				className={`mobile-drawer-content ${props.className || ''} `}
			>
				<SocialMediaShare
					className="social-media-share-close-hidden"
				/>
            </div>
        );
}
MobileDrawerContent.propTypes = {
	className: PropTypes.string,
	isOpen: PropTypes.bool,
};

export default MobileDrawerContent;