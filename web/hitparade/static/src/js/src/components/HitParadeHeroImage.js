import React, { PropTypes } from 'react';
import HitParadeLogo from './HitParadeLogo';
import HitParadeButton from './HitParadeButton';
import siteContent from '../../siteContent';
import { scroller } from 'react-scroll';

const HitParadeHeroImage = props => {
  return (
        <div className="hp-hero">
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
                    <section className="hp-hero-overlay-text hp-hero-overlay-large-text niveau-grotesk-black">
                        <div className="hp-hero-text-elem hp-hero-text-elm-large">WIN YOUR FAVORITE</div>
                    </section>
                    <section className="hp-hero-overlay-text hp-hero-overlay-medium-text niveau-grotesk-black"><div className="hp-hero-text-elem">FANTASY GAME TODAY!</div></section>
                    <section className="hp-hero-overlay-text hp-hero-bottom-overlay extra-bottom-space">
                    <HitParadeButton
                        className="hp-homepage-button niveau-grotesk-black"
                        buttonText="See How it Works"
                        clickMethod={() => props.scrollTo.howItWorks()}/>
                    <div
                        className="hp-homepage-arrow-container"
                        onClick={() => props.scrollTo.howItWorks()}
                    >
                        <div 
                            className="animated infinite bounce"
                        >
                            <img src={props.imgRoot+'arrow.svg'} />
                        </div>
                    </div>
                </section>
            </section>
            </div>
        );
}
HitParadeHeroImage.propTypes = {
    img: PropTypes.string.isRequired,
    navs: PropTypes.object.isRequired,
    scrollTo: PropTypes.object.isRequired,
};
export default HitParadeHeroImage;
