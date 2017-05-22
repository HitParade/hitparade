import React, { PropTypes } from 'react';
import HitParadeLogo from './HitParadeLogo';
import HitParadeButton from './HitParadeButton';
//data-0="opacity: 1;top: 64px;" data--500-top="opacity: 0; top: -500px;"
const HitParadeHeroImage = props => {
  return (
            <section id="slide1"
                     className="hp-hero-image">
                <section className="hp-hero-image-container-overlay"></section>
                <section className="hp-hero-image-container"
                     data-center="background-position: 50% 0px;" data-top-bottom="background-position: 50% -100px;" data-anchor-target="#slide1">
            	<section className="hp-hero-image-overlay" data-center="top: 0px; opacity: 1" data--150-top="top: -1200px; opacity: 1" data-anchor-target="#slide1 .hp-hero-image-overlay">
            		<section className="hp-hero-overlay-text hp-hero-overlay-small-text niveau-grotesk-black">
                        <div className="hp-hero-text-elem">START YOUR  </div><div className="hp-logo-hero-img-container"><HitParadeLogo className="hp-logo-hero-img" logoColor="#ffffff" logoWidth="206px" logoHeight="71px" logoViewBox="0 0 126 43"/></div>
       <div className="hp-hero-text-elem">TODAY AND</div></section>
            		<section className="hp-hero-overlay-text hp-hero-overlay-large-text niveau-grotesk-black"><div className="hp-hero-text-elem">WIN THE  </div><div className="hp-hero-text-elem">$5.6 </div>
                    </section>
            		<section className="hp-hero-overlay-text hp-hero-overlay-medium-text niveau-grotesk-black"><div className="hp-hero-text-elem">MILLION PRIZE</div></section>
            		<section className="hp-hero-overlay-text"><HitParadeButton className="hp-hide hp-homepage-button niveau-grotesk-black" buttonText="SEE THE PLAYERS"  clickMethod={props.navs.click.navSelectPlayers} /></section>
            	</section>
                <img src={ props.imgRoot+ props.img} className="hp-desktop-hero-image" style={{width: '100%',height: 'auto', maxHeight: '600px'}} />
                <img src={ props.imgRoot+ props.imgMobile} className="hp-mobile-hero-image" style={{width: '100%',height: 'auto', maxHeight: '600px'}} />
                </section>
            </section>
        );
}
HitParadeHeroImage.propTypes = {
    img: PropTypes.string.isRequired,
    navs: PropTypes.object.isRequired,
};

export default HitParadeHeroImage;
