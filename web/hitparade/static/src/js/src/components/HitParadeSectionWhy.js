import React, { PropTypes } from 'react';
import HitParadeButton from './HitParadeButton';
import Parallax from 'react-springy-parallax';
const HitParadeSectionWhy = props => {
  return (
       <Parallax.Layer
                            offset={1.1}
                            speed={-0.1}
							onClick={() => props.parallax}>

								  <div className="hp-why-content">
										<div className="hp-section-why-header">
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
									</div>
										<div className="hp-why-coin-image-container"
											 data-170-center="opacity: 1;transform: scale( 1.0 ); "
											 data-200-center="opacity: 1;transform: scale( 1.3 ); "
											 data-220-center="opacity: 0.01; transform:  scale( 0.1 ); ">
											<img src={props.imgRoot +'coins.svg'}  className="hp-why-coin-image" />
										</div>
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

									<div className="hp-section-why-footer">
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
									</div>
									</div>
           </Parallax.Layer>

        );
}
HitParadeSectionWhy.propTypes = {
	navs: PropTypes.object.isRequired,
	refs: PropTypes.object.isRequired,
    parallax: PropTypes.func.isRequired,
};

export default HitParadeSectionWhy;
