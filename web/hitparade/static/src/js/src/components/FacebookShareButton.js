import React, { PropTypes } from 'react';
import siteContent from '../../siteContent.js';

const FacebookShareButton = props => {
  return (
        <div 
            className="fb-share-button" 
            data-href="https://developers.facebook.com/docs/plugins/" 
            data-layout="button" data-size="large" data-mobile-iframe="true">
                <a 
                    className="fb-xfbml-parse-ignore" 
                    target="_blank" 
                    href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse"
                >
                    <img
                        className={ !props.iconSrc ? "fb-share-button-icon" : props.iconSrc }
                        src={siteContent.assets.facebookF}/>
                </a>
            </div>
        );
}
FacebookShareButton.propTypes = {
};

export default FacebookShareButton;