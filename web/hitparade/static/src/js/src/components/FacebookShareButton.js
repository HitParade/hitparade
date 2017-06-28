import React, { PropTypes } from 'react';
import siteContent from '../../siteContent.js';

const FacebookShareButton = props => {
  const url = encodeURI(siteContent.url)
  return (
        <div 
            className="fb-share-button" 
            data-href={url} 
            data-layout="button" data-size="large" data-mobile-iframe="true">
                <a 
                    className="fb-xfbml-parse-ignore" 
                    target="_blank" 
                    href={`https://www.facebook.com/sharer/sharer.php?u=${url}&amp;src=sdkpreparse`}
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