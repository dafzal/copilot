import React from 'react'
import { Segment, Header, Image, Button } from 'semantic-ui-react'

const Styles = {
	banner: {
		position: 'absolute',
		top: 10,
		right: 10
	},
	title: {
		color: 'white',
		position: 'absolute',
		left: 40,
		top: 60,
		textAlign: 'center'
	},
	incidents: {
		color: 'white',
		position: 'relative',
		left: 40,
		top: 100,
		fontSize: 50
	},
	drivers: {
		color: 'white',
		position: 'relative',
		left: 140,
		top: 100,
		fontSize: 50
	}
}

export default class HeadBanner extends React.Component {
	render() {
		return (
			<div>
				<Image src="../static/dist/assets/Header.png" />
				<Button style={Styles.banner}> Alerts </Button>
			</div>
		)
	}
}
