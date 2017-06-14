import React, { PropTypes } from 'react';
import HitParadeLogo from './HitParadeLogo';
import HitParadeButton from './HitParadeButton';
import Parallax from 'react-springy-parallax';
const HitParadeHeroImage = props => {
  return (
        <div className="">
                <Parallax.Layer
                    offset={0}
                    speed={0.5}
                    onClick={() => props.parallax}>

                    <section className="hp-hero-image-container"
                                data-center="background-position: 50% 0px;" data-top-bottom="background-position: 50% -100px;" data-anchor-target="#slide1">

                            </section>
                            <section className="hp-hero-image-container-overlay">
                            </section>
                            <section className="hp-hero-image-overlay" data-center="top: 0px; opacity: 1" data--150-top="top: -1200px; opacity: 1" data-anchor-target="#slide1 .hp-hero-image-overlay">
                            <section className="hp-hero-overlay-text hp-hero-overlay-small-text niveau-grotesk-black">
                                <div className="hp-hero-text-elem">
                                    START YOUR  
                                </div>

                                    <HitParadeLogo className="hp-logo-hero-img" logoColor="#ffffff" logoWidth="100% " logoHeight="100%" logoViewBox="0 0 126 43"/>
                                <div className="hp-hero-text-elem">
                                    TODAY AND
                                </div>
                            </section>
                            <section className="hp-hero-overlay-text hp-hero-overlay-large-text niveau-grotesk-black"><div className="hp-hero-text-elem">WIN THE  </div><div className="hp-hero-text-elem">$5.6 </div>
                            </section>
                            <section className="hp-hero-overlay-text hp-hero-overlay-medium-text niveau-grotesk-black"><div className="hp-hero-text-elem">MILLION PRIZE</div></section>
                            <section className="hp-hero-overlay-text hp-hero-bottom-overlay">
                            <HitParadeButton
                                className="hp-homepage-button niveau-grotesk-black"
                                buttonText="SEE THE PLAYERS"
                                clickMethod={props.parallax}/>
                            <div
                                className="hp-homepage-arrow-container"
                                onClick={props.parallax.bind(this)}
                            >
                                <div 
                                    className="animated infinite bounce"
                                >
                                    <img src={props.imgRoot+'arrow.svg'} />
                                </div>
                            </div>
                        </section>`
                    </section>
               </Parallax.Layer>
            </div>
        );
}
HitParadeHeroImage.propTypes = {
    img: PropTypes.string.isRequired,
    navs: PropTypes.object.isRequired,
    parallax: PropTypes.func.isRequired,
};
export default HitParadeHeroImage;
