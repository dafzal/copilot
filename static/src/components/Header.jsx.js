import React from 'react'
import { Segment, Header, Image, Message } from 'semantic-ui-react'
import $ from 'jquery'

var setHeight = function() {
	let height = document.getElementByClassName('.banner').style.height
	console.log(height)
	return height / 2
}
const Styles = {
	header: {
		position: 'relative',
		height: 'auto'
	},
	columns: {
		position: 'absolute',
		top: 120,
		left: 40,
		fontSize: 28,
		color: 'white',
		columns: 2
	}
}
export default class HeadBanner extends React.Component {
	constructor(props) {
		super(props)
		this.screenClick = this.screenClick.bind(this)
	}

	screenClick(e) {
		this.props.changeScreen(e.target.id)
	}

	render() {
		return (
			<div>
				<img className="banner" />
				<div style={Styles.columns}>
					<div onClick={this.screenClick} id="incident">
						{this.props.incident} Incidents
					</div>
					<div onClick={this.screenClick} id="user">
						{this.props.user} Users
					</div>
				</div>
			</div>
		)
	}
}
