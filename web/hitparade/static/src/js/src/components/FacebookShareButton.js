import React from 'react'; 
import PropTypes from 'prop-types';
import siteContent from '../../siteContent.js';

const FacebookShareButton = props => {
  const url = encodeURI(siteContent.url)
  return (
            <div 
                className="facebbook-share-button"
            >
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