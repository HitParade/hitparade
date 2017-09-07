import React, { PropTypes } from 'react';
import HitParadeButton from './HitParadeButton';
import Diamonds from './Diamonds';
import { responsive }   from '../../responsive';

const HitParadeSectionWhy = props => {
  const isMobile = responsive('isMobile');
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
					<img src={props.imgRoot + 'Mobile-Stats1.svg'}  className="hp-why-coin-image" />
				</div>
				<section className="hp-why-main-content">
					<section className="hp-why-header-bottom">
						<section className="hp-why-header-bottom-text proxima-nova-regular">
							Using more than 40 relevant data points per player, Hit Parade's artificial intelligence capabilities provide a new level of insight for professional and fantasy managers.
						</section>
						<section className="hp-why-header-bottom-panel-main">
							<section className="hp-why-header-bottom-panel">
									<section className="hp-why-register-text  niveau-grotesk-black">REGISTER FOR EARLY ACCESS</section>
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
