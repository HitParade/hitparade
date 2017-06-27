import React, { PropTypes } from 'react';
import FacebookShareButton from './FacebookShareButton';
import siteContent from '../../siteContent.js';

const SocialMediaShare = props => {
  return (
            <div className="social-media-share-container">
                <h2 
                  className="social-media-share-container-header niveau-grotesk-black"
                >
                  { siteContent.content.share.header }
                </h2>
                <FacebookShareButton/>
            </div>
        );
}

SocialMediaShare.propTypes = {
};

export default SocialMediaShare;