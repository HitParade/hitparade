import {
	NAV_FAQ,
	TERMS_OF_USE,
	NAV_CLOSE_MODAL,
	NAV_SIGNUP,
	NAV_LOGIN,
	NAV_CONTACT,
	SELECT_PLAYER,
	REMOVE_PLAYER,
	NAV_SELECT_PLAYERS,
	CART,
	NAV_SHARE,
	NAV_PRIVACY_STATEMENT,
	TOGGLE_HAMBRUGER,
} from '../actiontypes/hitparade';

const svgShare = {
  	img: 'share.svg',
  	width: '15px',
  	height: '16px',
  	maxHeight: '16px',
  };
const svgContact = {
	 	img: 'copy.svg',
	  	width: '15px',
	  	height: '16px',
	  	maxHeight: '16px',
  } ;
const svgCart = {
  		img: 'cart.png',
  		width: '20px',
  		height: '20px',
  		maxHeight: '20px',
  };
const initialState = {
	imgRoot: '/static/dist/images/',
	cart: [{}],
	playersInCart: 4,
	heroImage: 'Hero.png',
	heroImageMobile: 'heroImageMobile.svg',
	showModal: false,
	showDrawer: false,
	svgs: {
		svgContact: svgContact,
		svgShare: svgShare,
		svgCart: svgCart,
	},
};

const HitParade = {
  state: initialState, 
  actions: {
	[NAV_CLOSE_MODAL]: (state, action) => {
		return {
			...state,
			showModal: false,
		};
	},
	[NAV_SIGNUP]: (state, action) => {
		return {
			...state,
			showModal: true,
			modalData: 'signUp'
		};
	},
	[SELECT_PLAYER]: (state, action) => {
		return {
			...state,
			playersInCart: state.playersInCart += 1
		}
	},
	[REMOVE_PLAYER]: (state, action) => {
		return {
			...state,
			playersInCart: (state.playersInCart-1),
		};

	},
	[TOGGLE_HAMBRUGER]: (state, action) => {
		return {
			...state,
			showDrawer: !state.showDrawer
		};

	},
	[NAV_LOGIN]: (state, action) => state,
	[NAV_SELECT_PLAYERS]: (staet, action) => state,
	[NAV_FAQ]: (state, action) => state,
	[NAV_CONTACT]: (state, action) => state,
	[TERMS_OF_USE]: (state, action) => state,
	[CART]: (state, action) => state,
	[NAV_SHARE]: (state, action) => {
		return {
			...state,
			showModal: true,
			modalData: 'share'
		}
	},
	[NAV_PRIVACY_STATEMENT]: (state, action) => state,
  }
};

