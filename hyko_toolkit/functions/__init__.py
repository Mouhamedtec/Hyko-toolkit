# Register Functions

from .converters.markdown_to_pdf.metadata import func as func  # noqa: F811
from .converters.ocr_pdf_to_text.metadata import func as func  # noqa: F811
from .converters.pdf_to_text.metadata import func as func  # noqa: F811
from .converters.video_converter.metadata import func as func  # noqa: F811
from .converters.video_to_audio.metadata import func as func  # noqa: F811
from .downloaders.pdf_downloader.metadata import func as func  # noqa: F811
from .downloaders.youtube_downloader.metadata import (  # noqa: F811
    func as func,
)
from .plotting.bivariate_plot.metadata import func as func  # noqa: F811
from .plotting.univariate_plot.metadata import func as func  # noqa: F811
from .utils.nlp_utils.recursive_character_text_splitter.metadata import (
    func as func,  # noqa: F811
)
from .utils.nlp_utils.remove_stopwords.metadata import func as func  # noqa: F811
from .web.web_scraping.beautifulsoup_transformer.metadata import (
    func as func,  # noqa: F811
)
from .web.web_scraping.html2text_transformer.metadata import func as func  # noqa: F811
from .web.web_scraping.youtube_transcript.metadata import func as func  # noqa: F811
from .web.web_search.duckduckgo_search.metadata import (
    func as func,  # noqa: F811
)
from .web.web_search.wikipedia_search.metadata import (
    func as func,  # noqa: F811
)
