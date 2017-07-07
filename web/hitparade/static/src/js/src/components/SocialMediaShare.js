import React from 'react'; 
import PropTypes from 'prop-types';
import FacebookShareButton from './FacebookShareButton';
import TwitterShareButton from './TwitterShareButton';
import siteContent from '../../siteContent.js';

const SocialMediaShare = props => {
  return (
            <div className="social-media-share-container">
                <img 
                  src={siteContent.assets.closeIcon}  
                  className="social-media-share-close" 
                  onClick={() => props.closeModal()} 
                />
                <h2 
                  className="social-media-share-container-header niveau-grotesk-black"
                >
                  { siteContent.content.share.header }
                </h2>
                <FacebookShareButton/>
                <TwitterShareButton/>
            </div>
        );
}

SocialMediaShare.propTypes = {
};

export default SocialMediaShare;