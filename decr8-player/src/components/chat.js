// Step 1: Import React. This lets you use JSX inside your .js file.
import * as React from 'react'
import { useStaticQuery, graphql } from 'gatsby'
import chatData from "../chat/chat.yaml"

const yaml = require('js-yaml');

const query = useStaticQuery(graphql`
{
  allChatYaml {
    edges {
      node {
        title
      }
    }
  }
}
`)
 
/* Step 2: Define your component. Note that your
component name should start with a capital letter. */
const Chat = () => {
    // chat setup
    const [msgData, setMsgData] = useState({})
    const inputRef = useRef(null);
    // const currentlyPlaying = data.allFile.nodes.map(node => node.name);
    const { allChatYaml } = data
    
    const handleSubmit = (event) => {
	event.preventDefault()
	if (inputRef.current.value !== "") { 	
	    const { name, value } = event.target
	    setMsgData({ ...msgData, [name]: value })
	    chatData.content.push({ "item" : inputRef.current.value })
	}
	inputRef.current.value = ""
    }
    
    return (
	<div className="chat-container">
	    <div className="chat">
		<h1>{chatData.title}</h1>
		<ul>
		    {chatData.content.map((data, index) => {
			return <li key={`content_item_${index}`}>
				   {data.item}
			       </li>
		    })}
		</ul>
	    </div>
	    <input
		className="chat-bar"
		type="text"
		ref={inputRef}
		placeholder="chat..."
		required
		autoComplete="off"
	    />
	    <button
		className="chat-button"
		type="submit"
		onClick={handleSubmit}
	    >
		💬
	    </button>
	</div>

    )
}

/* Step 3: Export your component so it
   can be used by other parts of your app. */
export default Chat
