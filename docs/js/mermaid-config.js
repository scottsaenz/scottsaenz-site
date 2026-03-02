mermaid.initialize({
  theme: 'base',
  themeVariables: {
    primaryColor: '#e1f5fe',
    primaryTextColor: '#000',
    primaryBorderColor: '#2196f3',
    lineColor: '#333',
    secondaryColor: '#f3e5f5',
    tertiaryColor: '#fff3e0',
    fontFamily: 'inherit'
  }
});

function setExternalLinksToNewTab() {
  const links = document.querySelectorAll('a[href]');

  for (const link of links) {
    const href = link.getAttribute('href');

    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
      continue;
    }

    let parsedUrl;
    try {
      parsedUrl = new URL(href, window.location.href);
    } catch {
      continue;
    }

    const isHttp = parsedUrl.protocol === 'http:' || parsedUrl.protocol === 'https:';
    const isExternal = parsedUrl.origin !== window.location.origin;

    if (isHttp && isExternal) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  }
}

if (typeof document$ !== 'undefined') {
  document$.subscribe(setExternalLinksToNewTab);
} else {
  document.addEventListener('DOMContentLoaded', setExternalLinksToNewTab);
}