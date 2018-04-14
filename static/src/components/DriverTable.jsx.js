import React from 'react'
import DayBox from './DayBox.jsx.js'
import { Segment, Header } from 'semantic-ui-react'

export default class DriverTable extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<div>
				<DayBox date={'APRIL 14'} />
				<DayBox date={'APRIL 15'} />
				<DayBox date={'APRIL 16'} />
			</div>
		)
	}
}
