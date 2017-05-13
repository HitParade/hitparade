import React, { PropTypes } from 'react';
import HitParadeButton from './HitParadeButton';

const HitParadeSectionWhy = props => {
  return (
            <section className="hp-section-why">

            		<header className="hp-section-why-header">
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'}  className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'}className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            		</header>
            		<main className="hp-why-content">
            			<section className="hp-why-coin-image-container">
            				<img src={props.imgRoot +'coins.svg'}  className="hp-why-coin-image" />
            			</section>
            			<section className="hp-why-main-content">
            					<section className="hp-why-header-top niveau-grotesk-black">
            						BEAT THE STREAK FOR THE COST OF YOUR MORNING COFFEE
            					</section>
            					<section className="hp-why-header-divider">
            						<img src={props.imgRoot +'divider.svg'}   className="hp-divider" />
            					</section>
            					<section className="hp-why-header-bottom">
            						<section className="hp-why-header-bottom-text proxima-nova-regular">
            							Hit Parade provides detailed statistics in order to predict whether or not a player will get a hit in the upcoming games.
            						</section>
            						<section className="hp-why-header-bottom-panel-main">
	            						<section className="hp-why-header-bottom-panel">
		            							<section className="hp-why-register-text  niveau-grotesk-black">REGISTER FOR EARLY ACCESS</section>
		            							<section className="hp-why-register-text-desc proxima-nova-regular">Get Free Access for 1 week.</section>
		            					</section>
	            						<section className="hp-why-register-button"><HitParadeButton className="hp-why-register-button niveau-grotesk-black " buttonText="REGISTER TODAY"  clickMethod={props.navs.click.navSignup} /></section>
	            					</section>

            					</section>
            			</section>

            		</main>
            		<footer className="hp-section-why-footer">
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            			<div className="hp-section-diamond">
            				<img src={props.imgRoot +'diamond.svg'} className="hp-section-why-header-diamond" />
            			</div>
            		</footer>
            </section>
        );
}
HitParadeSectionWhy.propTypes = {
	navs: PropTypes.object.isRequired,
};

export default HitParadeSectionWhy;
