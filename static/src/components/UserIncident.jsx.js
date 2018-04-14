import React from 'react'
import {
	Segment,
	Header,
	Image,
	Table,
	Modal,
	Button,
	Input
} from 'semantic-ui-react'
import $ from 'jquery'
import Chart from 'chart.js'

const Styles = {
	truncate: {
		whiteSpace: 'nowrap',
		overflow: 'hidden',
		textOverflow: 'ellipsis'
	}
}

export default class UserIncident extends React.Component {
	constructor(props) {
		super(props)
		this.handleClose = this.handleClose.bind(this)
		this.onOpen = this.onOpen.bind(this)
		this.state = {
			issue: '',
			modalOpen: false
		}
	}

	handleClose() {
		this.setState({ modalOpen: false })
	}
	onOpen() {
		this.setState({ modalOpen: true })
	}

	render() {
		let data = this.props.data
		let user = data.user
		return (
			<Table.Row>
				<Table.Cell>{data.timestamp}</Table.Cell>

				<Table.Cell>
					<div style={Styles.truncate}>{data.incident_id}</div>
				</Table.Cell>
				<Table.Cell>{data.issue}</Table.Cell>
				<Table.Cell>
					<Modal
						trigger={
							<Button onClick={this.onOpen} basic>
								See More
							</Button>
						}
					>
						<Modal.Header>Review Incident</Modal.Header>
						<Modal.Content>
							<Image.Group size="small">
								{data.img_urls.map(pic => <Image src={pic} />)}
							</Image.Group>
						</Modal.Content>
					</Modal>
				</Table.Cell>
			</Table.Row>
		)
	}
}
