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

const Styles = {
	truncate: {
		width: 200,
		whiteSpace: 'nowrap',
		overflow: 'hidden',
		textOverflow: 'ellipsis'
	}
}

export default class Incident extends React.Component {
	constructor(props) {
		super(props)
		this.input = this.input.bind(this)
		this.submit = this.submit.bind(this)
		this.state = {
			issue: ''
		}
	}
	input(e, d) {
		this.setState({ issue: d.value })
	}
	submit() {
		//ajax call to api to send status
	}
	render() {
		let data = this.props.data
		let user = data.user
		return (
			<Table.Row>
				<Table.Cell>{data.timestamp}</Table.Cell>
				<Table.Cell>
					<Header as="h4" image>
						<Image src={user.img_url} rounded size="mini" />
						<Header.Content>
							{user.name}
							<Header.Subheader>
								<div style={Styles.truncate}>
									{user.user_id}
								</div>
							</Header.Subheader>
						</Header.Content>
					</Header>
				</Table.Cell>
				<Table.Cell>
					<div style={Styles.truncate}>{data.incident_id}</div>
				</Table.Cell>
				<Table.Cell>
					{data.reviewed_at
						? 'Reviewed at ' + data.reviewed_at
						: 'Needs Review'}
				</Table.Cell>
				<Table.Cell>{data.issue ? data.issue : ''}</Table.Cell>
				<Table.Cell>
					<Modal
						trigger={
							<Button
								basic
								color={data.reviewed_at ? 'green' : 'red'}
							>
								{data.reviewed_at ? 'See More' : 'Review Now'}
							</Button>
						}
					>
						<Modal.Header>Review Incident</Modal.Header>
						<Modal.Content>
							<Image.Group size="small">
								{data.img_urls.map(pic => <Image src={pic} />)}
							</Image.Group>
						</Modal.Content>
						<Modal.Actions>
							<Modal
								trigger={
									<Button
										basic
										color={
											data.reviewed_at ? 'green' : 'red'
										}
									>
										{data.reviewed_at
											? 'Review Again'
											: 'Review Now'}
									</Button>
								}
							>
								<Modal.Header>Submit Report</Modal.Header>
								<Modal.Content>
									<Input
										placeholder="Search..."
										onChange={this.input}
									/>
								</Modal.Content>
								<Modal.Actions>
									{' '}
									<Button onClick={this.submit}>
										Submit
									</Button>
								</Modal.Actions>
							</Modal>
						</Modal.Actions>
					</Modal>
				</Table.Cell>
			</Table.Row>
		)
	}
}
