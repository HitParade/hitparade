import React, { PropTypes } from 'react';
import HitParadeLogo from './HitParadeLogo';
import HitParadeButton from './HitParadeButton';
const HitParadeHeroImage = props => {
  return (
            <section className="hp-hero-image">
            	<section className="hp-hero-image-overlay">
            		<section className="hp-hero-overlay-text hp-hero-overlay-small-text niveau-grotesk-black">
                        <div className="hp-hero-text-elem">START YOUR  </div><div className="hp-logo-hero-img-container"><HitParadeLogo className="hp-logo-hero-img" logoColor="#2d2d2d" logoWidth="206px" logoHeight="71px" logoViewBox="0 0 126 43"/></div>
       <div className="hp-hero-text-elem">TODAY AND</div></section>
            		<section className="hp-hero-overlay-text hp-hero-overlay-large-text niveau-grotesk-black"><div className="hp-hero-text-elem">WIN THE   </div><img src={ props.imgRoot+'the5.6mil.svg'} className="hp-56mil-svg"/>
           </section>
            		<section className="hp-hero-overlay-text hp-hero-overlay-medium-text niveau-grotesk-black"><div className="hp-hero-text-elem">MILLION PRIZE</div></section>
            		<section className="hp-hero-overlay-text"><HitParadeButton className="hp-hide hp-homepage-button niveau-grotesk-black" buttonText="SEE THE PLAYERS"  clickMethod={props.navs.click.navSelectPlayers} /></section>
            	</section>
                <img src={ props.imgRoot+ props.img} className="hp-desktop-hero-image" style={{width: '100%',height: 'auto', maxHeight: '600px'}} />
                <img src={ props.imgRoot+ props.imgMobile} className="hp-mobile-hero-image" style={{width: '100%',height: 'auto', maxHeight: '600px'}} />
            </section>
        );
}
HitParadeHeroImage.propTypes = {
    img: PropTypes.string.isRequired,
    navs: PropTypes.object.isRequired,
};

export default HitParadeHeroImage;
