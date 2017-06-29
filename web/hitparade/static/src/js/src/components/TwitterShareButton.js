import React, { PropTypes } from 'react';
import siteContent from '../../siteContent.js';

const TwitterShareButton = props => {
  const { text, url } = siteContent.content.twitterIntent;
  const intentDestinationUrl = encodeURI(url);
  const intentText = encodeURI(text)
  const baseUrl = siteContent.externalLinks.twitterIntentBase;
  return (
            <div 
                className="twitter-share-button" 
            >
                <a
                    className="twitter-share-link"
                    href={`${baseUrl}?url=${intentDestinationUrl}&text=${intentText}`}
                >
                    <img
                        className={ !props.iconSrc ? "twitter-share-button-icon" : props.iconSrc }
                        src={siteContent.assets.twitter}/>
                </a>
            </div>
        );
}
TwitterShareButton.propTypes = {
};

export default TwitterShareButton;