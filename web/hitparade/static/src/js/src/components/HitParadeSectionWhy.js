import React, { PropTypes } from 'react';
import HitParadeButton from './HitParadeButton';
import Parallax from 'react-springy-parallax';
import Diamonds from './Diamonds';
import { responsive }   from '../../responsive';
import prallaxConfig from '../../parallaxConfig';

const HitParadeSectionWhy = props => {

  const isMobile = responsive('isMobile');
  const { offset, speed } = prallaxConfig.why;
  return (
		<div className="hp-why-content">
			<Diamonds 
				className="hp-section-why-header"
				count={isMobile ? "5" : "11"}
				src={props.imgRoot +'diamond.svg'}
			/>
		
			<div className="hp-why-container">
				<div className="hp-why-coin-image-container"
						data-170-center="opacity: 1;transform: scale( 1.0 ); "
						data-200-center="opacity: 1;transform: scale( 1.3 ); "
						data-220-center="opacity: 0.01; transform:  scale( 0.1 ); ">
					<img src={props.imgRoot + 'coins.svg'}  className="hp-why-coin-image" />
				</div>
				<section className="hp-why-main-content">
					<section className="hp-why-header-top niveau-grotesk-black">
						BEAT THE STREAK FOR THE COST OF YOUR MORNING COFFEE
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
							<section className="hp-why-header-bottom-panel-right">
								<HitParadeButton 
									className="hp-why-register-button niveau-grotesk-black " 
									buttonText="REGISTER TODAY"  
									clickMethod={props.navs.click.navSignup} 
								/>
							</section>
						</section>
					</section>
				</section>
			</div>
		<Diamonds 
			className="hp-section-why-footer"
			count={isMobile ? "5" : "11"}
			src={props.imgRoot +'diamond.svg'}
		/>
	</div>
	);
}
HitParadeSectionWhy.propTypes = {
	navs: PropTypes.object.isRequired,
	refs: PropTypes.object.isRequired,
    parallax: PropTypes.func.isRequired,
};

export default HitParadeSectionWhy;
